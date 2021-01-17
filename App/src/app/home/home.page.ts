import { Component } from '@angular/core';
import { PhotoService } from '../services/photo.service';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  constructor(public photoService: PhotoService, private apiService: ApiService ) { }

  takePhoto() {
    this.photoService.addNewToGallery();
    
  }

  getModel() {
    this.apiService.getData().subscribe(data => {
      console.log(data);
    });

  }

  sendData() {
    this.photoService.sendData();
  }
}
