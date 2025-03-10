package cvrankerback.cv;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CVRepository extends MongoRepository<CV, String> {
    List<CV> findByJobId(String jobId);
    List<CV> findByJobSeekerId(String jobSeekerId);
    long countByJobId(String jobId);
}