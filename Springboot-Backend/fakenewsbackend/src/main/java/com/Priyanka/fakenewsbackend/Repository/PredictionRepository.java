package com.Priyanka.fakenewsbackend.Repository;


import com.Priyanka.fakenewsbackend.Entity.prediction;

import org.springframework.data.jpa.repository.JpaRepository;

public interface PredictionRepository
        extends JpaRepository<prediction, Long> {

}