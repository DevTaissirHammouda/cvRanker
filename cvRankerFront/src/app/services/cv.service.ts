import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root',
})
export class CvService {
  private apiUrl = `${environment.apiBaseUrl}/api/cvs`;

  constructor(private http: HttpClient) {}

  uploadCV(cv: FormData): Observable<any> {
    return this.http.post(`${this.apiUrl}/upload`, cv);
  }

  downloadCV(cvId: string): Observable<Blob> {
    return this.http.get(`${this.apiUrl}/${cvId}/download`, { responseType: 'blob' });
  }
  getCvs(jobId:string): Observable<any> {
    return this.http.get(`${this.apiUrl}/job/${jobId}`);
  }
  selectCv(jobId:string,cvId:string): Observable<any> {
    return this.http.get(`${this.apiUrl}/select/${jobId}/${cvId}`);
  }
}
