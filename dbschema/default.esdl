module default {
    type User {
    required username: str {
        constraint exclusive;
    };
    required password: str;
    created_at: datetime {
            default := (datetime_current());
            readonly := true;
        };
        updated_at: datetime {
          rewrite update using (datetime_of_statement());
        };
    }

    type Post {
    required user: User;
    required text: str;
    created_at: datetime {
            default := (datetime_current());
            readonly := true;
        };
        updated_at: datetime {
          rewrite update using (datetime_of_statement());
        };
    }
}
