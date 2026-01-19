from django.db import models

class Team(models.Model):
    
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Player(models.Model):


    name=models.CharField(max_length=100)
    team=models.ForeignKey(Team,on_delete=models.CASCADE,related_name='Players')


    def __str__(self):
        return self.name



class Match(models.Model):

    team1=models.ForeignKey(Team, on_delete=models.CASCADE,related_name='team1_matches')
    team2=models.ForeignKey(Team, on_delete=models.CASCADE,related_name='team2_matches')


    start_date=models.DateTimeField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.team1}vs {self.team2}"



class Innings(models.Model):
    match=models.ForeignKey(Match, on_delete=models.CASCADE,related_name='innings')
    batting_team=models.ForeignKey(Team,on_delete=models.CASCADE)
    total_runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    overs = models.FloatField(default=0.0)





    def __str__(self):
        return f"{self.batting_team} innings"
    

    def update(self):

        balls=self.balls.all()

        total_runs=0
        wickets=0
        valid_balls=0

        for ball in balls:
            total_runs=total_runs+ball.runs

            if ball.is_wicket:
                wickets=wickets+1
            
            if not ball.is_extra:
                valid_balls=valid_balls+1


        self.total_runs = total_runs
        self.wickets = wickets
        self.overs = valid_balls // 6 + (valid_balls % 6) / 10
        self.save()




    



class Ball(models.Model):
    innings=models.ForeignKey(Innings,on_delete=models.CASCADE,related_name='balls')
    runs = models.IntegerField(default=0)
    is_wicket = models.BooleanField(default=False)
    is_extra = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # save the ball first
        self.innings.update()


