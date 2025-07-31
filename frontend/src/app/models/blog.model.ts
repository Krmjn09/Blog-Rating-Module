export interface Blog {
  id?: number;
  user_name: string;
  title: string;
  time?: Date;
  content: string;
  tag: string;
  likes: number;
  comments: number;
  rating: number;
}
