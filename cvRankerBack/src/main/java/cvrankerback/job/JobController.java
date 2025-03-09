package cvrankerback.job;

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
    public ResponseEntity<List<Job>> getAllJobs() {
        return ResponseEntity.ok(jobService.getAllJobs());
    }

    @GetMapping("/employer/{id}")
    public ResponseEntity<List<Job>> getJobsByEmployer(@PathVariable String id) {
        return ResponseEntity.ok(jobService.getJobsByEmployer(id));
    }
}