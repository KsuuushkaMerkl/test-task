CREATE MIGRATION m1oeje7jmhxnczankwxenckr5irhi5xi2xsu2phoii6apxeq5wb7hq
    ONTO m16tv2rcgp2t5hvbgos6ptn64ak5nrwyidklebfgl2zr2gdxsn3o6q
{
  ALTER TYPE default::User {
      ALTER PROPERTY username {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
