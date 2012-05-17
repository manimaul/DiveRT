ALTER TABLE cleanups ADD ownerpct CHAR;
ALTER TABLE cleanups ADD operapct CHAR;

INSERT INTO [settings] ([setting], [value]) VALUES ('version', 'DiveRT v1.07');