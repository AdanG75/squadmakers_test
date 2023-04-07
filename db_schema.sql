CREATE TABLE public.jokes (
    id_joke serial NOT NULL,
    joke character varying(999) NOT NULL,
    created_time timestamp without time zone DEFAULT LOCALTIMESTAMP NOT NULL,
    updated_time timestamp without time zone,
    dropped boolean DEFAULT false NOT NULL
);

ALTER TABLE ONLY public.jokes
    ADD CONSTRAINT jokes_pkey PRIMARY KEY (id_joke);

CREATE FUNCTION public.sp_trigger_jokes_before_update() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
	BEGIN
		-- SECURE IMPORTANT AND UNCHANGEABLE DATA
		NEW.id_joke := OLD.id_joke;
		NEW.created_time := OLD.created_time;
		-- OBTEIN UPDATE TIME
		NEW.updated_time := LOCALTIMESTAMP;
		-- REMOVE SPACES FROM BEGIN AND END OF DATA
		NEW.joke := BTRIM(NEW.joke);

		RETURN NEW;
	END;
$$;

CREATE TRIGGER tr_jokes_before_update BEFORE UPDATE ON public.jokes FOR EACH ROW EXECUTE FUNCTION public.sp_trigger_jokes_before_update();