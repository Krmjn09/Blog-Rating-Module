import { Routes } from '@angular/router';
import { BlogCreate } from './components/blog-create/blog-create';
import { BlogList } from './components/blog-list/blog-list';
import { BlogDetail } from './components/blog-detail/blog-detail';

export const routes: Routes = [
  { path: '', component: BlogList },
  { path: 'create', component: BlogCreate },
  { path: 'blog/:id', component: BlogDetail },
];
