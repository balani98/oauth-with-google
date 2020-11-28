import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(private http:HttpClient,private router:Router) { }

  ngOnInit(): void {
  }
  login(formObject){
      this.http.post('http://localhost:5000/login',formObject).subscribe((res)=>{
        localStorage.setItem('Authorization',`Bearer ${res['token']}`)
        if(res['success']==true)
          this.router.navigate(['home']);
        
      })
  }

}
