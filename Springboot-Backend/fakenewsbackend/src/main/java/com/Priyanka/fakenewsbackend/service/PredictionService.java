package com.Priyanka.fakenewsbackend.service;

import com.Priyanka.fakenewsbackend.dto.PredictionRequest;
import com.Priyanka.fakenewsbackend.dto.PredictionResponse;

public interface PredictionService {

    PredictionResponse checkNews(PredictionRequest request);
}