create schema stackoverflow_filtered;

set search_path to stackoverflow_filtered;

create table "results" (
	"user_id" int4,
	"display_name" text,
	"views" int4,
	"reputation" text,
	"updated_at" text,
	"created_at" text,
	"location" text,
	"city" text,
	"country" text,
	"questions_id" int4,
	"question_user_id" int4,
	"title" text,
	"body" text,
	"accepted_answer_id" int4,
	"score" int4,
	"view_count" int4,
	"comment_count" int4,
	"questions_created_at" text,
	"answer_id" int4,
	"answer_user_id" int4,
	"question_id" int4,
	"answers_body" text,
	"answers_score" int4,
	"answers_comment_count" int4,
	"answers_created_at" text
)

--Create a btree index on the reputation column within the results table.
CREATE INDEX reputation ON results (reputation);

--Create a hash index on the display_name column within the results table.
CREATE INDEX display_name ON results USING hash (display_name);


-- create a view
create view results_view as 
	select results.display_name, city, questions_id
	from results
	where accepted_answer_id IS NOT NULL;

--select * from results_view1

--DROP VIEW result_view1;

--Create a materialized view 
create materialized view results_view1 as 
	select results.display_name, city, questions_id
	from results
	where accepted_answer_id IS NOT NULL;



