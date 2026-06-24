package com.Priyanka.fakenewsbackend.Entity;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "predictions")
@Data
public class Prediction {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "input_text", columnDefinition = "TEXT")
    private String inputText;

    private String prediction;

    private Double confidence;
}