import { TestBed } from '@angular/core/testing';

import { CvTableService } from './cv-table.service';

describe('CvTableService', () => {
  let service: CvTableService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CvTableService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
