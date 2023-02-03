    @commands.slash_command(name="ping", description="Get a pong message with response time.")
    async def ping(self, ctx):
        start_time = time.time()
        embed = discord.Embed(description="Pong!", color=0x2f3136)
        response = await ctx.respond(embed=embed)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        embed.description = f"Pong! {duration:.2f}ms."
        await response.edit(embed=embed)
