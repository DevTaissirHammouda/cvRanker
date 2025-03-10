import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CvsTableComponent } from './cvs-table.component';

describe('CvsTableComponent', () => {
  let component: CvsTableComponent;
  let fixture: ComponentFixture<CvsTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CvsTableComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CvsTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
