import { Injectable } from '@angular/core';
import {BehaviorSubject} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class SharedInformationService {

  constructor() { }
  private _jobsId = new BehaviorSubject<String>("");

  setJobId(jobId: String) {
    this._jobsId.next(jobId);
  }
  getJobId(): BehaviorSubject<String> {
    return this._jobsId;
  }
}
