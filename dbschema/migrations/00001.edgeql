CREATE MIGRATION m16tv2rcgp2t5hvbgos6ptn64ak5nrwyidklebfgl2zr2gdxsn3o6q
    ONTO initial
{
  CREATE TYPE default::User {
      CREATE PROPERTY created_at: std::datetime {
          SET default := (std::datetime_current());
          SET readonly := true;
      };
      CREATE REQUIRED PROPERTY password: std::str;
      CREATE PROPERTY updated_at: std::datetime {
          CREATE REWRITE
              UPDATE 
              USING (std::datetime_of_statement());
      };
      CREATE REQUIRED PROPERTY username: std::str;
  };
  CREATE TYPE default::Post {
      CREATE REQUIRED LINK user: default::User;
      CREATE PROPERTY created_at: std::datetime {
          SET default := (std::datetime_current());
          SET readonly := true;
      };
      CREATE REQUIRED PROPERTY text: std::str;
      CREATE PROPERTY updated_at: std::datetime {
          CREATE REWRITE
              UPDATE 
              USING (std::datetime_of_statement());
      };
  };
};
