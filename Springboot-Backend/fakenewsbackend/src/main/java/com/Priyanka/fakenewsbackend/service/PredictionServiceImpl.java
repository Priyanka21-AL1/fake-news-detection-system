package com.Priyanka.fakenewsbackend.service;

import com.Priyanka.fakenewsbackend.dto.PredictionRequest;
import com.Priyanka.fakenewsbackend.dto.PredictionResponse;
import com.Priyanka.fakenewsbackend.Entity.Prediction;
import com.Priyanka.fakenewsbackend.Repository.PredictionRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.time.LocalDateTime;

@Service
public class PredictionServiceImpl implements PredictionService {

    @Autowired
    private PredictionRepository repository;

    private final RestTemplate restTemplate = new RestTemplate();

    @Override
    public PredictionResponse checkNews(PredictionRequest request) {

        String FASTAPI_URL = "http://127.0.0.1:8000/predict";

        PredictionResponse response =
                restTemplate.postForObject(
                        FASTAPI_URL,
                        request,
                        PredictionResponse.class
                );

        Prediction prediction = new Prediction();

        prediction.setInputText(request.getText());
        prediction.setPrediction(response.getPrediction());
        prediction.setConfidence(response.getConfidence());
        prediction.setCreatedAt(LocalDateTime.now());

        repository.save(prediction);

        return response;
    }
}