from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io
import os

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = load_model("C:/model/medicine_model.h5")

# Get class names from training folder
train_dir = "C:/model_split/train"
class_names = sorted(os.listdir(train_dir))

# Dictionary for medicine usage info
medicine_usage = {
    "aggrex": "used to treat peptic ulcers, irritable bowel syndrome (IBS), and enterocolitis by reducing stomach acid and relieving abdominal cramps",
    "paramol": "Relieves pain, fever, inflammation from arthritis, back pain, toothache, and headaches.",
    "zantac": "Relieves heartburn, acid indigestion, peptic ulcers, and GERD by reducing stomach acid.",
    "czinc": "Supports immune function, wound healing, and provides antioxidant protection.",
    "clindasol": "Treats acne and bacterial skin infections topically.",
    "fucidin": "Treats bacterial skin infections like impetigo, boils, and infected wounds.",
    "fucicort": "Manages inflammatory skin conditions with bacterial or fungal infections like eczema.",
    "rheumatizen": "Provides relief from muscle and joint pain, arthritis, sprains, and backache.",
    "congestal": "Relieves common cold and flu symptoms including congestion, pain, and fever.",
    "daflon": "Treats chronic venous insufficiency, varicose veins, and hemorrhoids.",
    "dipofort": "Treats vitamin B12 deficiency anemia and related neurological issues.",
    "cemicresto": "Lowers high cholesterol and triglycerides while increasing good cholesterol (HDL) to prevent heart attacks, strokes, and cardiovascular disease.",
    "carbamide": "Treats dry, rough skin conditions like psoriasis, eczema, ichthyosis, calluses, and corns by moisturizing, exfoliating, and softening the skin.",
    "cetal sinus": "Relieves sinus congestion, nasal pain, headache, fever, and upper respiratory symptoms from colds, flu, sinusitis, and rhinitis.",
    "choleroze": "Lowers high cholesterol and triglycerides while increasing good cholesterol (HDL) to prevent heart attacks, strokes, and cardiovascular disease.",
    "diclac": "Relieves pain, inflammation, and swelling in arthritis, muscle strains, back pain, and rheumatic conditions with extended-release action.",
    "diflucan": "Treats fungal infections such as vaginal thrush, oral candidiasis, esophageal candidiasis, and other systemic fungal infections.",
    "milga": "Treats neuritis, neuralgia, polyneuropathies (diabetic, alcoholic), nerve pain, herpes zoster, facial palsy, and vitamin B deficiencies as a nerve tonic.",
    "mucosta": "Treats gastric ulcers, acute/chronic gastritis, and protects gastric mucosa from erosion, bleeding, and inflammation.",
    "selokenz": "Treats high blood pressure, angina, irregular heart rhythms, heart failure, and prevents migraines and heart attacks.",
    "zenta": "Treats acid reflux, heartburn, peptic ulcers, GERD, and Zollinger-Ellison syndrome by reducing stomach acid production.",
    # Add more medicines here as needed
}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img = img.resize((224, 224))
    x = np.array(img) / 255.0
    x = np.expand_dims(x, axis=0)

    pred = model.predict(x)
    label = class_names[np.argmax(pred)]
    confidence = float(np.max(pred))

    usage = medicine_usage.get(label, "Usage information not available")

    return {"medicine": label, "confidence": confidence, "usage": usage}
