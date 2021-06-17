/*
 Navicat Premium Data Transfer

 Source Server         : 194.99.21.140
 Source Server Type    : PostgreSQL
 Source Server Version : 120005
 Source Host           : 194.99.21.140:5433
 Source Catalog        : safebull
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 120005
 File Encoding         : 65001

 Date: 18/06/2021 02:38:27
*/


-- ----------------------------
-- Sequence structure for lang_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."lang_id_seq";
CREATE SEQUENCE "public"."lang_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for tokens_output_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."tokens_output_id_seq";
CREATE SEQUENCE "public"."tokens_output_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Table structure for invite_accruals
-- ----------------------------
DROP TABLE IF EXISTS "public"."invite_accruals";
CREATE TABLE "public"."invite_accruals" (
  "inviting_user_id" int4 NOT NULL,
  "invited_id" int4 NOT NULL,
  "created_date_time" timestamp(6) NOT NULL,
  "tokens" int4 NOT NULL
)
;

-- ----------------------------
-- Records of invite_accruals
-- ----------------------------

-- ----------------------------
-- Table structure for lang
-- ----------------------------
DROP TABLE IF EXISTS "public"."lang";
CREATE TABLE "public"."lang" (
  "id" int4 NOT NULL DEFAULT nextval('lang_id_seq'::regclass),
  "code" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of lang
-- ----------------------------
INSERT INTO "public"."lang" VALUES (1, 'ru');
INSERT INTO "public"."lang" VALUES (2, 'en');

-- ----------------------------
-- Table structure for tokens_output
-- ----------------------------
DROP TABLE IF EXISTS "public"."tokens_output";
CREATE TABLE "public"."tokens_output" (
  "user_id" int4 NOT NULL,
  "tokens" int4,
  "created_date_time" timestamp(6),
  "id" int4 DEFAULT nextval('tokens_output_id_seq'::regclass)
)
;

-- ----------------------------
-- Records of tokens_output
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "public"."user";
CREATE TABLE "public"."user" (
  "id" int4 NOT NULL,
  "name" text COLLATE "pg_catalog"."default",
  "created_date_time" timestamp(6) NOT NULL,
  "begin_captcha" bool NOT NULL DEFAULT false,
  "accept_rules" bool NOT NULL DEFAULT false,
  "refferrer_id" int4,
  "tokens" int4 NOT NULL DEFAULT 0,
  "lang_id" int4 NOT NULL DEFAULT 1,
  "is_banned" bool NOT NULL DEFAULT false,
  "bep_address" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of user
-- ----------------------------

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."lang_id_seq"
OWNED BY "public"."lang"."id";
SELECT setval('"public"."lang_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
SELECT setval('"public"."tokens_output_id_seq"', 5, true);

-- ----------------------------
-- Primary Key structure for table invite_accruals
-- ----------------------------
ALTER TABLE "public"."invite_accruals" ADD CONSTRAINT "invite_accruals_pkey" PRIMARY KEY ("inviting_user_id", "invited_id");

-- ----------------------------
-- Primary Key structure for table lang
-- ----------------------------
ALTER TABLE "public"."lang" ADD CONSTRAINT "lang_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table tokens_output
-- ----------------------------
ALTER TABLE "public"."tokens_output" ADD CONSTRAINT "tokens_output_pkey" PRIMARY KEY ("user_id");

-- ----------------------------
-- Primary Key structure for table user
-- ----------------------------
ALTER TABLE "public"."user" ADD CONSTRAINT "user_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table invite_accruals
-- ----------------------------
ALTER TABLE "public"."invite_accruals" ADD CONSTRAINT "invite_accruals_invited_id_fkey" FOREIGN KEY ("invited_id") REFERENCES "public"."user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."invite_accruals" ADD CONSTRAINT "invite_accruals_inviting_user_id_fkey" FOREIGN KEY ("inviting_user_id") REFERENCES "public"."user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table tokens_output
-- ----------------------------
ALTER TABLE "public"."tokens_output" ADD CONSTRAINT "tokens_output_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table user
-- ----------------------------
ALTER TABLE "public"."user" ADD CONSTRAINT "user_lang_id_fkey" FOREIGN KEY ("lang_id") REFERENCES "public"."lang" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
