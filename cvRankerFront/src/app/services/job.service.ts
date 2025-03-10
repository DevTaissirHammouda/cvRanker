import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root',
})
export class JobService {
  private apiUrl = `${environment.apiBaseUrl}/api/jobs`;
  constructor(private http: HttpClient) {}

  postJob(job: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/post`, job);
  }

  getJobs(): Observable<any> {
    return this.http.get(`${this.apiUrl}/all`);
  }

  getJobsByEmployer(employerEmail: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/employer/${employerEmail}`);
  }
}
