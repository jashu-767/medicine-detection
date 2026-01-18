package com.medicinedetection.controller;

import com.medicinedetection.util.MultipartInputStreamFileResource;
import org.springframework.http.*;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import java.util.Map;

@CrossOrigin(origins = "http://localhost:3000")  
@RestController
@RequestMapping("/api/medicine")
public class MedicineController {

    @PostMapping("/detect")
    public ResponseEntity<?> detectMedicine(@RequestParam("file") MultipartFile file) {
        try {
            String mlUrl = "http://localhost:8000/predict"; 

            RestTemplate restTemplate = new RestTemplate();
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.MULTIPART_FORM_DATA);

            MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();
            body.add("file", new MultipartInputStreamFileResource(file.getInputStream(), file.getOriginalFilename()));

            HttpEntity<MultiValueMap<String, Object>> requestEntity = new HttpEntity<>(body, headers);
            ResponseEntity<Map> response = restTemplate.postForEntity(mlUrl, requestEntity, Map.class);

            return ResponseEntity.ok(response.getBody());  
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body(Map.of("error", "Failed to process file", "details", e.getMessage()));
        }
    }
}
