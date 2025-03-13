import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CvPostModalComponent } from './cv-post-modal.component';

describe('CvPostModalComponent', () => {
  let component: CvPostModalComponent;
  let fixture: ComponentFixture<CvPostModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CvPostModalComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CvPostModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
