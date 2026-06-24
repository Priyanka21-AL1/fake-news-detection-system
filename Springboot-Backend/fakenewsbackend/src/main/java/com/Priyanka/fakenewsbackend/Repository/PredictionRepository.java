package com.Priyanka.fakenewsbackend.Repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.Priyanka.fakenewsbackend.Entity.Prediction;

@Repository
public interface PredictionRepository
        extends JpaRepository<Prediction, Long> {

}