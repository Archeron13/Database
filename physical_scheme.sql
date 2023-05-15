create schema restaurant;

create table restaurant.customer(
    cust_id int primary key,
    cust_name char(50) not null
);

create table restaurant.employees(
    emp_id int primary key,
    job char(50),
    present bool not null,
    emp_sal int not null
);

create table restaurant.tables(
    table_no int primary key,
    cust_id int,
    emp_id int not null,
    addit_req text,

    foreign key (cust_id) references restaurant.customer(cust_id),
    foreign key (emp_id) references restaurant.employees(emp_id)
);

create table restaurant.orders(
    order_id int primary key,
    cust_id int,
    table_no int,
    cost int not null,

    foreign key (cust_id) references restaurant.customer(cust_id),
    foreign key (table_no) references restaurant.tables(table_no)
);

create table restaurant.bar(
    drink_id int,
    order_id int not null,
    drink_avail bool,
    drink_cost int not null,

    foreign key (order_id) references restaurant.orders(order_id)
);

create table restaurant.dishes(
    dish_id int primary key,
    order_id int not null,
    est_time int,

    foreign key (order_id) references restaurant.orders(order_id)
);

create table restaurant.raw_ingredient(
    ing_id int,
    ing_name char(50),
    dish_id int,
    avail bool not null,

    foreign key (dish_id) references restaurant.dishes(dish_id)
);

create table restaurant.corporation(
    corp_id int primary key,
    table_no int,
    discount int not null,
    corp_name char(50),

    foreign key (table_no) references restaurant.tables(table_no)
);
