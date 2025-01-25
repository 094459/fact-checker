-- Users table to store user information
CREATE TABLE "users" (
    "user_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user" TEXT NOT NULL,
    "email" TEXT NOT NULL UNIQUE,
    "password_hash" TEXT NOT NULL,
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "last_login" TIMESTAMP
);

-- Categories table for fact categorization
CREATE TABLE "categories" (
    "category_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL UNIQUE,
    "description" TEXT
);

-- Facts table to store the main fact entries
CREATE TABLE "facts" (
    "fact_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER NOT NULL,
    "category_id" INTEGER NOT NULL,
    "content" TEXT NOT NULL,
    "supporting_url" TEXT,
    "supporting_info" TEXT,
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("user_id") REFERENCES "users" ("user_id"),
    FOREIGN KEY ("category_id") REFERENCES "categories" ("category_id")
);

-- Votes table to track user votes on facts
CREATE TABLE "votes" (
    "vote_id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "fact_id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "vote_type" TEXT CHECK(vote_type IN ('Fact', 'Fake')) NOT NULL,
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("fact_id") REFERENCES "facts" ("fact_id"),
    FOREIGN KEY ("user_id") REFERENCES "users" ("user_id"),
    UNIQUE ("fact_id", "user_id")
);
