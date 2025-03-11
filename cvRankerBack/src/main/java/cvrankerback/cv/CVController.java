package cvrankerback.cv;

import cvrankerback.cv.DTO.CVsDto;
import lombok.RequiredArgsConstructor;
import org.apache.commons.io.IOUtils;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/cvs")
@RequiredArgsConstructor
public class CVController {
    private final CVService cvService;
    private final CVRepository cvRepository;

    @PostMapping("/upload")
    public ResponseEntity<CV> uploadCV(@RequestParam("jobSeekerId") String jobSeekerId,
                                       @RequestParam("jobId") String jobId,
                                       @RequestParam("file") MultipartFile file) throws IOException {
        CV cv = CV.builder()
                .jobSeekerId(jobSeekerId)
                .jobId(jobId)
                .fileName(file.getOriginalFilename())
                .fileType(file.getContentType())
                .fileData(file.getBytes())
                .build();
        return ResponseEntity.ok(cvService.uploadCV(cv));
    }

    @GetMapping("/{cvId}/download")
    public ResponseEntity<byte[]> downloadCV(@PathVariable String cvId) {
        Optional<CV> cv = cvRepository.findById(cvId);
        if (cv.isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok()
                .contentType(MediaType.parseMediaType(cv.get().getFileType()))
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + cv.get().getFileName() + "\"")
                .body(cv.get().getFileData());
    }

    @GetMapping("/job/{jobId}")
    public ResponseEntity<List<CVsDto>> getCVsByJob(@PathVariable String jobId) {
        return ResponseEntity.ok(cvService.getCVsByJob(jobId));
    }

    @GetMapping("/select/{jobId}/{cvId}")
    public ResponseEntity<?> selectCV(@PathVariable String jobId, @PathVariable String cvId) {
        return cvService.selectCV(jobId, cvId);
    }
}
