import { CanActivateFn, Router } from '@angular/router';

export const tokenGuard: CanActivateFn = (route, state) => {
  const token = localStorage.getItem('token');

  if (token) {
    return true; // Allow access
  } else {
    const router = new Router();
    router.navigate(['/login']); // Redirect to login if no token
    return false;
  }
};

