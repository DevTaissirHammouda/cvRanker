import { Injectable } from '@angular/core';
import {BehaviorSubject} from "rxjs";
import {CvModel} from "../components/cvs-table/cvModel";

@Injectable({
  providedIn: 'root'
})
export class CvTableService {


  private _cvsBs = new BehaviorSubject<CvModel[]>([]);

  constructor() { }

  getCvs(): BehaviorSubject<CvModel[]> {
    return this._cvsBs;
  }
  setCvs(data: CvModel[],selectedCV:string) {
    //if selected is not "none" then set the cv with same id first
    if(selectedCV!=="none"){
      const selectedCv=data.find(cv=>cv.id===selectedCV)
      if(selectedCv){
        data=[selectedCv,...data.filter(cv=>cv.id!==selectedCV)]
      }
    }
    this._cvsBs.next(data);
  }

  addCv(cv: CvModel) {
    const newList = this._cvsBs.value;
    newList.push(cv);
    this._cvsBs.next(newList);
  }

  deleteCv(cv: CvModel) {
    const newList = this._cvsBs.value.filter(j => j.id !== cv.id);
    this._cvsBs.next(newList);
  }
}
