package com.Priyanka.fakenewsbackend.service;

import java.util.Map;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class NewsService {

    public Map<String, Object> getPrediction(String text) {

        RestTemplate restTemplate = new RestTemplate();

        Map<String, String> request =
                Map.of("text", text);

        return restTemplate.postForObject(
                "http://127.0.0.1:8000/predict",
                request,
                Map.class
        );
    }
}