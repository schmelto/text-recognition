import { Injectable } from '@angular/core';
import { Plugins, CameraResultType, CameraSource } from '@capacitor/core';
import { ApiService } from './api.service';

const { Camera } = Plugins;

@Injectable({
  providedIn: 'root'
})
export class PhotoService {

  public photos: Photo[] = [];

  constructor(private apiService: ApiService) { }

  public async addNewToGallery() {

    const capturedPhoto = await Camera.getPhoto({
      resultType: CameraResultType.Uri, 
      source: CameraSource.Camera, 
      quality: 100 
    });
  
    this.photos.unshift({
      filepath: "soon...",
      webviewPath: capturedPhoto.webPath
    });
  }

  public async sendData(){
    this.apiService.sendData(this.photos).subscribe(data => {
      console.log(data);
    });
  }
}

export interface Photo {
  filepath: string;
  webviewPath: string;
}