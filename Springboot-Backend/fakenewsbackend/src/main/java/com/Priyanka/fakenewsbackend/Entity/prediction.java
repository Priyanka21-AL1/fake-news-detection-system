package com.Priyanka.fakenewsbackend.Entity;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "predictions")
@Data


public class prediction {
     @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(columnDefinition = "TEXT")
    private String inputText;

    private String prediction;

    private Double confidence;
}
