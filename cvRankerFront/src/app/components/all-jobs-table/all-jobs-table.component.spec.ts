import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AllJobsTableComponent } from './all-jobs-table.component';

describe('AllJobsTableComponent', () => {
  let component: AllJobsTableComponent;
  let fixture: ComponentFixture<AllJobsTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AllJobsTableComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AllJobsTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
