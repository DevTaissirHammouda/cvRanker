package cvrankerback.cv;

import lombok.RequiredArgsConstructor;
import org.apache.commons.io.IOUtils;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.List;

@RestController
@RequestMapping("/api/cvs")
@RequiredArgsConstructor
public class CVController {
    private final CVService cvService;

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
        CV cv = cvService.getCVsByJob(cvId).get(0);
        return ResponseEntity.ok()
                .contentType(MediaType.parseMediaType(cv.getFileType()))
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + cv.getFileName() + "\"")
                .body(cv.getFileData());
    }
}