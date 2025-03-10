import { Injectable } from '@angular/core';
import {BehaviorSubject} from "rxjs";
import {JobModel} from "../components/jobs-table/jobModel";

@Injectable({
  providedIn: 'root'
})
export class JobTableService {

  private _jobsBs = new BehaviorSubject<JobModel[]>([]);

  constructor() { }

  getJobs(): BehaviorSubject<JobModel[]> {
    return this._jobsBs;
  }
  setJobs(data: JobModel[]) {
    this._jobsBs.next(data);
  }

  addJob(job: JobModel) {
    const newList = this._jobsBs.value;
    newList.push(job);
    this._jobsBs.next(newList);
  }

  deleteJob(job: JobModel) {
    const newList = this._jobsBs.value.filter(j => j.id !== job.id);
    this._jobsBs.next(newList);
  }

}
