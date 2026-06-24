package com.Priyanka.fakenewsbackend.dto;

public class PredictionResponse {

    private String prediction;
    private Double confidence;

    public String getPrediction() {
        return prediction;
    }

    public void setPrediction(String prediction) {
        this.prediction = prediction;
    }

    public Double getConfidence() {
        return confidence;
    }

    public void setConfidence(Double confidence) {
        this.confidence = confidence;
    }
}