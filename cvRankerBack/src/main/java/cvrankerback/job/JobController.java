package cvrankerback.job;

import cvrankerback.job.dto.jobDto;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/jobs")
@RequiredArgsConstructor
public class JobController {
    private final JobService jobService;

    @PostMapping("/post")
    public ResponseEntity<Job> postJob(@RequestBody Job job) {
        Job savedJob = jobService.postJob(job);
        return ResponseEntity.ok(savedJob);
    }

    @GetMapping("/all")
    public ResponseEntity<List<jobDto>> getAllJobs() {
        return ResponseEntity.ok(jobService.getAllJobs());
    }

    @GetMapping("/employer/{email}")
    public ResponseEntity<List<jobDto>> getJobsByEmployer(@PathVariable String email) {
        return ResponseEntity.ok(jobService.getJobsByEmployer(email));
    }

}
