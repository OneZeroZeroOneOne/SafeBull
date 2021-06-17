CREATE TABLE "user" (
  "id" int PRIMARY KEY,
  "name" text,
  "created_date_time" timestamp,
  "begin_captcha" bool,
  "assept_ruls" bool,
  "refferrer_id" int,
  "tokens" int,
  "lang_id" int
);

CREATE TABLE "lang" (
  "id" SERIAL PRIMARY KEY,
  "code" text
);

CREATE TABLE "group_activity" (
  "user_id" int PRIMARY KEY,
  "last_check" timestamp
);

ALTER TABLE "group_activity" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");

ALTER TABLE "user" ADD FOREIGN KEY ("lang_id") REFERENCES "lang" ("id");
