
class MultiHeadAttention(nn.Module):
    
    
    
    def forward(self,q,k,v,n_head,mask=None,):
        batch,time,dimension=q.shape
        n_d=dimension//n_head
        q=q.view(batch,time,n_head,n_d).permute(0,2,1,3)
        k=k.view(batch,time,n_head,n_d).permute(0,2,1,3)
        v=v.view(batch,time,n_head,n_d).permute(0,2,1,3)
        socre=q@k.transpose(2,3)/math.sqrt(d)
        if mask is not None:
            mask=torch.trill(torch.ones(time,time,dytype=bool))
            score=score.masked_fill(mask==0,-inf)
        socre=softmax(socre,dimension=-1)
        socre=score@v
        score=score.permute(0,2,1,3).contigous().view(batch,time,dimension)
        score=self.linear(score)
        
        return score





 