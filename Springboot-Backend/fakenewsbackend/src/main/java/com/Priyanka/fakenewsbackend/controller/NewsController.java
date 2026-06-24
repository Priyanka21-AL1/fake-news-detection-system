package com.Priyanka.fakenewsbackend.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class NewsController {
     @GetMapping("/")
    public String home() {
        return "Fake News Detection Backend Running";
}
}
