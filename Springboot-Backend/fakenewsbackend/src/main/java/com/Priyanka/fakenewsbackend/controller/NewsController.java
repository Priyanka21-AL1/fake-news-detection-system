package com.Priyanka.fakenewsbackend.controller;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.Priyanka.fakenewsbackend.Entity.Prediction;
import com.Priyanka.fakenewsbackend.Repository.PredictionRepository;
import com.Priyanka.fakenewsbackend.dto.NewsRequest;
import com.Priyanka.fakenewsbackend.service.NewsService;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/api/news")
public class NewsController {

    @Autowired
    private NewsService newsService;

    @Autowired
    private PredictionRepository predictionRepository;

    @GetMapping("/")
    public String home() {
        return "Fake News Detection Backend Running";
    }

    @PostMapping("/check")
    public Map<String, Object> checkNews(
            @RequestBody NewsRequest request) {

        Map<String, Object> result =
                newsService.getPrediction(
                        request.getText()
                );

        System.out.println(result);

        Prediction prediction =
                new Prediction();

        prediction.setInputText(
                request.getText()
        );

        prediction.setPrediction(
                result.get("prediction")
                        .toString()
        );

        prediction.setConfidence(
                Double.parseDouble(
                        result.get("confidence")
                                .toString()
                )
        );

        predictionRepository.save(
                prediction
        );

        return result;
    }

    @GetMapping("/history")
    public Object getHistory() {
        return predictionRepository.findAll();
    }
}