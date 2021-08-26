-- DROP TRIGGER insert_survey_answer
CREATE TRIGGER IF NOT EXISTS insert_survey_answer
AFTER INSERT ON survey_answer
BEGIN
   UPDATE survey_question SET active=0, ranking=0;
   
   -- Run OK in SQLLITE3, Solve all Cases; But Not Accepted in DJANGO
   /*
   UPDATE "survey_question" SET ranking=ifnull(T.points,0)
   FROM (SELECT question_id,ifnull(SUM(survey_answer.like*5-survey_answer.dislike*3),0) AS points FROM survey_question, survey_answer WHERE survey_question.id = survey_answer.question_id GROUP BY survey_question.id ) AS T 
   WHERE survey_question.id = T.question_id;
   */
   -- Run OK in SQLLITE3, Solve all Cases, ... DJANGO
   DELETE FROM survey_point;
   INSERT INTO survey_point(question_id, score)
   SELECT question_id,ifnull(SUM(survey_answer.like*5-survey_answer.dislike*3),0) FROM survey_question, survey_answer WHERE survey_question.id = survey_answer.question_id GROUP BY survey_question.id;
   --
   -- UPDATE survey_question SET ranking=ifnull(survey_point.score,0) FROM survey_point WHERE survey_question.id = survey_point.question_id;
   UPDATE survey_question SET ranking=( SELECT ifnull(survey_point.score,0) FROM survey_point WHERE survey_question.id = survey_point.question_id)
   WHERE survey_question.id IN (SELECT survey_point.question_id FROM survey_point WHERE survey_question.id = survey_point.question_id);
   
   UPDATE survey_question SET ranking = ifnull(ranking,0) + 10*( SELECT count(survey_answer.question_id) FROM survey_answer WHERE survey_question.id = survey_answer.question_id );   
   UPDATE survey_question SET ranking = ifnull(ranking,0) + 10  WHERE round((julianday('now') - julianday(created))) = 0; 
   UPDATE survey_question SET active=1 where id IN (SELECT id FROM survey_question ORDER BY ranking DESC LIMIT 4 );
END;
   