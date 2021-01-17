import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

// const API_URL = environment.apiUrl;
const API_URL = 'http://127.0.0.1:5000';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  getData() {
    return this.http.get(`${API_URL}/model`);
  }

  sendData(data) {
    console.log(data);
    return this.http.post<any>(`${API_URL}/model`, data);
  }
}