import { Component } from '@angular/core';
import { JobService } from '../../services/job.service';

@Component({
  selector: 'app-job-posting',
  templateUrl: './job-posting.component.html',
  styleUrls: ['./job-posting.component.css'],
})
export class JobPostingComponent {
  job = {
    title: '',
    description: '',
    companyName: '',
    postedBy: '', // Employer email
  };

  constructor(private jobService: JobService) {}

  onSubmit() {
console.log(localStorage.getItem('email'))
      this.job.postedBy = localStorage.getItem('email')!.toString();

    this.jobService.postJob(this.job).subscribe((response) => {
      console.log('Job posted successfully!', response);
    });
  }
}
