package com.medicinedetection.service;

import com.medicinedetection.model.Medicine;
import com.medicinedetection.repository.MedicineRepository;
import org.springframework.stereotype.Service;

@Service
public class MedicineService {
    private final MedicineRepository repository;

    public MedicineService(MedicineRepository repository) {
        this.repository = repository;
    }

    public Medicine saveMedicine(String name, double confidence) {
        Medicine medicine = new Medicine(name, confidence);
        return repository.save(medicine);
    }
}
