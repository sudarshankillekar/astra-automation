import { sqliteTable, text } from 'drizzle-orm/sqlite-core';
export const enquiries = sqliteTable('enquiries', {
  id: text('id').primaryKey(),
  name: text('name').notNull(),
  business: text('business').notNull(),
  phone: text('phone').notNull(),
  email: text('email').notNull(),
  industry: text('industry').notNull(),
  need: text('need').notNull(),
  message: text('message').notNull(),
  createdAt: text('created_at').notNull(),
});
