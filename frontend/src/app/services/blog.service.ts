import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Blog } from '../models/blog.model';

@Injectable({
  providedIn: 'root'
})
export class BlogService {
  private apiUrl = 'http://127.0.0.1:8000/api/blogs/';  // Django backend URL

  constructor(private http: HttpClient) {}

  // Get all blogs
  getBlogs(): Observable<Blog[]> {
    return this.http.get<Blog[]>(this.apiUrl);
  }

  // Get a single blog by ID
  getBlog(id: number): Observable<Blog> {
  return this.http.get<Blog>(`${this.apiUrl}${id}/`);
}


  // Create a new blog
  createBlog(blog: Blog): Observable<Blog> {
    return this.http.post<Blog>(this.apiUrl, blog);
  }

  // Update a blog
  updateBlog(id: number, blog: Blog): Observable<Blog> {
    return this.http.put<Blog>(`${this.apiUrl}${id}/`, blog);
  }

  // Delete a blog
  deleteBlog(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}${id}/`);
  }
}
