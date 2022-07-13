//
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

//Servicios
import { DashboardService } from './servicios/dashboard.service';
import { BasictableService } from './servicios/basictable.service';


//rutaS
import { APP_ROUTING } from './app.routes';
import { from } from 'rxjs';
import { AsideComponent } from './aside/aside.component';
import { TopbarComponent } from './topbar/topbar.component';
import { FooterComponent } from './footer/footer.component';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ProfileComponent } from './profile/profile.component';
import { BasictableComponent } from './basictable/basictable.component';
import { BlankComponent } from './blank/blank.component';
import { Error404Component } from './error404/error404.component';
import { FontawesomeComponent } from './fontawesome/fontawesome.component';
import { MapgoogleComponent } from './mapgoogle/mapgoogle.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { GraficoComponent } from './grafico/grafico.component';

import { NgChartsModule } from 'ng2-charts';
import { TablarealComponent } from './tablareal/tablareal.component';


@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    ProfileComponent,
    BasictableComponent,
    BlankComponent,
    Error404Component,
    FontawesomeComponent,
    MapgoogleComponent,
    AsideComponent,
    TopbarComponent,
    FooterComponent,
    GraficoComponent,
    TablarealComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    APP_ROUTING,
    NgChartsModule
  ],
  providers: [
    DashboardService,
    BasictableService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
