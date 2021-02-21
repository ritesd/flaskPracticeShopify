CREATE TABLE product (
    product_id BIGINT,
	title varchar(255),
	vendor varchar(255),
	status BOOL,
	varients_id BIGINT,
    created_at datetime default now(),
    updated_at datetime default now(),
    PRIMARY KEY (product_id, varients_id)
);

CREATE TABLE orders (
	order_id BIGINT,
	product_id BIGINT,
	varients_id BIGINT,
	order_status bool,
	response_json JSON,
	created_at datetime default now(),
	updated_at datetime default now(),
	PRIMARY KEY (order_id)
);

INSERT INTO product(product_id, title, vendor, status, varients_id) VALUES (4635585314883,
 '09I8ZQ8UGQ',
 'MishiPayTestDevelopmentEmptyStore',
 1,
 32328279588931);