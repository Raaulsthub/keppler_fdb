create database Kepler;

use Kepler;

create table Corpo_Celeste (
	co_id int unsigned auto_increment,
	co_nome varchar(255) unique, 
    co_massa float, 
    co_massa_erro1 float, 
    co_massa_erro2 float, 
    co_raio float, 
    co_raio_erro1 float, 
    co_raio_erro2 float,
    primary key(co_id));

select count(*) from Corpo_Celeste;

create table Estrela (
	st_id int unsigned,
	st_asc_str varchar(255),
    st_asc double,
    st_dec_str varchar(255),
    st_dec double,
    st_dist float, 
    st_dist_erro1 float, 
    st_dist_erro2 float, 
    st_opt_mag float, 
    st_mag_erro float, 
    st_faixa_mag varchar(255), 
    st_temp float, 
    st_temp_erro1 float, 
    st_temp_erro2 float, 
    primary key(st_id),
    foreign key(st_id) references Corpo_Celeste(co_id));
    
select count(*) from Estrela;

create table Planeta (
	pl_id int unsigned,
    st_id int unsigned,
    pl_met_desc varchar(255),
    pl_orb_per float,
    pl_orb_per_erro1 float,
    pl_orb_per_erro2 float,
    pl_orb_comp float,
    pl_orb_comp_erro1 float,
    pl_orb_comp_erro2 float,
    pl_orb_exc float,
    pl_orb_exc_erro1 float,
    pl_orb_exc_erro2 float,
    pl_orb_inc float,
    pl_orb_inc_erro1 float,
    pl_orb_inc_erro2 float,
    pl_massa_prov varchar(255),
    pl_dens float,
    pl_dens_erro1 float,
    pl_dens_erro2 float,
    pl_vtt bool,
    pl_n_notas int,
    pl_atz date,
    primary key(pl_id),
    foreign key(pl_id) references Corpo_Celeste(co_id),
    foreign key(st_id) references Estrela(st_id));
    
select count(*) from Planeta;