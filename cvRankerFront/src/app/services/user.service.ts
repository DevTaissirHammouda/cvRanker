import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private apiUrl = `${environment.apiBaseUrl}/api/users`; // Set your backend API base URL here

  constructor(private http: HttpClient) {}

  // Register user
  registerUser(user: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/register`, user);
  }

  // Login user
  loginUser(credentials: { email: string; password: string }): Observable<any> {
    const params = new HttpParams()
      .set('email', credentials.email)
      .set('password', credentials.password);

    return this.http.post<any>(`${this.apiUrl}/login`, params);
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('role');
  }

}
